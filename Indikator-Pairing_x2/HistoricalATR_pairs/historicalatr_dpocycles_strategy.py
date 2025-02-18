import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'DPOCycles': 1.0
        })
    )
