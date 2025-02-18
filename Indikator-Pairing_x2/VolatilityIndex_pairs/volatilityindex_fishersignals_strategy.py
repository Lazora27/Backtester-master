import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
