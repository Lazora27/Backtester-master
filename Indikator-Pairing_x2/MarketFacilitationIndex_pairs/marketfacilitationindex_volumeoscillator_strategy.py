import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
