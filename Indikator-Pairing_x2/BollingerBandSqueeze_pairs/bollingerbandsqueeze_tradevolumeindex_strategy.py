import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
