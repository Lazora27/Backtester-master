import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
