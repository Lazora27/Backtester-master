import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'HistoricalATR': 1.0
        })
    )
