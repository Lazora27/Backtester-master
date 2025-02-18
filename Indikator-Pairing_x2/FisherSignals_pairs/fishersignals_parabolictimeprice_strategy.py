import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
