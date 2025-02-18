import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und FisherSignals
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'FisherSignals': 1.0
        })
    )
