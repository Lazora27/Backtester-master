import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
