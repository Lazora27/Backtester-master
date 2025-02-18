import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'FisherSignals': 1.0
        })
    )
