import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SeasonalStrength': 1.0
        })
    )
