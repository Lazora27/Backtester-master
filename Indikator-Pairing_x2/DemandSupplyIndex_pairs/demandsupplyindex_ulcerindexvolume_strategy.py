import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
