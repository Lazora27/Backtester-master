import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VWAPBands': 1.0
        })
    )
