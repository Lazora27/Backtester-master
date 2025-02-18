import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'FisherSignals': 1.0
        })
    )
