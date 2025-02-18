import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DetrendedPriceIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
