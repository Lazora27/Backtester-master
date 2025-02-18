import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SeasonalStrength': 1.0
        })
    )
