import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'FisherSignals': 1.0
        })
    )
