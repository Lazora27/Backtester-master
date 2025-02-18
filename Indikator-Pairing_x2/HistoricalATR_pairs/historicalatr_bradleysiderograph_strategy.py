import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'BradleySiderograph': 1.0
        })
    )
