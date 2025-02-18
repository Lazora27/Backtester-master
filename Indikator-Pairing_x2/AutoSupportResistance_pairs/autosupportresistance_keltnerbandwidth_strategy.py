import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
