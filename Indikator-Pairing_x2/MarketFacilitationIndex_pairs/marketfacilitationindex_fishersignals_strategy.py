import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
