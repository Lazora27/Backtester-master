import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
