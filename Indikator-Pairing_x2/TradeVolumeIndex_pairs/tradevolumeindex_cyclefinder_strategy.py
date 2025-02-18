import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
