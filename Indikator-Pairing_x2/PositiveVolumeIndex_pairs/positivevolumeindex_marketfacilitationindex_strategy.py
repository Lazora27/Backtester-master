import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
