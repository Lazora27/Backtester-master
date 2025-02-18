import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und BarStrength
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'BarStrength': 1.0
        })
    )
