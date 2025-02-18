import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VolumeDelta': 1.0
        })
    )
