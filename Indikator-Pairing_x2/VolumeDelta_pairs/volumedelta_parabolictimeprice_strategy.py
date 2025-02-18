import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
