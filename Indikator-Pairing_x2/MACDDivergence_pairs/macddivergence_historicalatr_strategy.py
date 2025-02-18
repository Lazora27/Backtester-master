import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HistoricalATR': 1.0
        })
    )
