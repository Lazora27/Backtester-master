import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
