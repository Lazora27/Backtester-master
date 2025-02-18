import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'FisherSignals': 1.0
        })
    )
