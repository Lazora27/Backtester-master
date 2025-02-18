import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FisherSignals': 1.0
        })
    )
