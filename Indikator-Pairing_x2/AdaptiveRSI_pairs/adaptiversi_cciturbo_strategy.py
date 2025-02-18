import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
