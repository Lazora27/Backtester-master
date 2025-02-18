import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'CenterOfGravity': 1.0
        })
    )
