import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und GannAngles
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'GannAngles': 1.0
        })
    )
