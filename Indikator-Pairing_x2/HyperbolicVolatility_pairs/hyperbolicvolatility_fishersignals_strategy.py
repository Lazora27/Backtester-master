import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'FisherSignals': 1.0
        })
    )
