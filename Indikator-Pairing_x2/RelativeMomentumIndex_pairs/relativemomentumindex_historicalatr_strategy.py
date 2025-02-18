import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
