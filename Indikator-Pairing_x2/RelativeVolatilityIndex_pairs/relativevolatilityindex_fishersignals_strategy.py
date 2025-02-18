import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVolatilityIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVolatilityIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RelativeVolatilityIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
