import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'FisherSignals': 1.0
        })
    )
