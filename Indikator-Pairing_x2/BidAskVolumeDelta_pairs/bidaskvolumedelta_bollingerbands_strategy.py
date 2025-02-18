import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und BollingerBands
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'BollingerBands': 1.0
        })
    )
