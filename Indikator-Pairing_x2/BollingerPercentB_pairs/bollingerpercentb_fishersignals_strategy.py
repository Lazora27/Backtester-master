import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'FisherSignals': 1.0
        })
    )
