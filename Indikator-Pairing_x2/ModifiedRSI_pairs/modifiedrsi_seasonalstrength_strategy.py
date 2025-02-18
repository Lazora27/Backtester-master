import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
