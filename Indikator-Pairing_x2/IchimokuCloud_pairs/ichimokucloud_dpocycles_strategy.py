import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und DPOCycles
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'DPOCycles': 1.0
        })
    )
