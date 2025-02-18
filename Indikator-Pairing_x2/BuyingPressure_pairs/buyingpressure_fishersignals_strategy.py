import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'FisherSignals': 1.0
        })
    )
