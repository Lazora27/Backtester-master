import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VolumeDelta': 1.0
        })
    )
