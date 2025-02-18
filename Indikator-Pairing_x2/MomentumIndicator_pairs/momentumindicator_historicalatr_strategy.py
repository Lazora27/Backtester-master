import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
