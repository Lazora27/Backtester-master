import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
