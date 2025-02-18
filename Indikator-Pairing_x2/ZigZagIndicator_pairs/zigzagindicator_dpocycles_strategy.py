import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
