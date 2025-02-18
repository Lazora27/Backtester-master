import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
