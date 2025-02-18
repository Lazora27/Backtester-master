import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'DPOCycles': 1.0
        })
    )
