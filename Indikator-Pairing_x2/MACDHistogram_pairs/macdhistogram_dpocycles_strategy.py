import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DPOCycles': 1.0
        })
    )
