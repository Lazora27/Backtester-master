import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
