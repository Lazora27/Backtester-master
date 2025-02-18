import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
