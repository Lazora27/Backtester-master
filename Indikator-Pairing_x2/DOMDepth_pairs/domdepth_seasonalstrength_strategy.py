import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SeasonalStrength': 1.0
        })
    )
