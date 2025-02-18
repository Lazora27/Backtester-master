import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HistoricalATR': 1.0
        })
    )
