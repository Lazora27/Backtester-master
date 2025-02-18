import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'FisherSignals': 1.0
        })
    )
